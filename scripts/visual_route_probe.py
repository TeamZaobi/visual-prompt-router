#!/usr/bin/env python3
"""Emit a small local readiness report for visual-route selection."""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


HELP_TIMEOUT_SECS = 8
MAC_APPS = {
    "Google Chrome": "/Applications/Google Chrome.app",
    "Microsoft Edge": "/Applications/Microsoft Edge.app",
    "Safari": "/Applications/Safari.app",
}


def _run(cmd: list[str]) -> dict[str, object]:
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=HELP_TIMEOUT_SECS,
            check=False,
        )
    except FileNotFoundError:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": "missing"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": "timeout"}
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def _probe_command(name: str) -> dict[str, object]:
    path = shutil.which(name)
    if not path:
        return {"available": False, "path": None}

    help_result = _run([name, "--help"])
    preview = help_result["stdout"].splitlines()[:6] if help_result["stdout"] else []
    return {
        "available": True,
        "path": path,
        "help_ok": help_result["ok"],
        "help_preview": preview,
    }


def _probe_mac_apps() -> dict[str, dict[str, object]]:
    return {
        name: {"exists": Path(bundle).exists(), "bundle": bundle}
        for name, bundle in MAC_APPS.items()
    }


def _route_readiness(commands: dict[str, dict[str, object]], apps: dict[str, dict[str, object]]) -> dict[str, dict[str, str]]:
    gemini_ready = commands["gemini"]["available"]
    playwright_ready = commands["playwright"]["available"]
    browser_present = any(app["exists"] for app in apps.values())

    return {
        "prompt_only": {
            "status": "ready",
            "reason": "Prompt delivery does not depend on local execution tools.",
        },
        "built_in_image": {
            "status": "host-specific",
            "reason": "This must be confirmed from the current host tool surface, not from shell probes.",
        },
        "gemini_cli": {
            "status": "installed" if gemini_ready else "missing",
            "reason": (
                "Gemini CLI shell surface is present. Image-specific subcommands or extensions still need host verification."
                if gemini_ready
                else "The gemini executable is not in PATH."
            ),
        },
        "browser_create_image": {
            "status": (
                "partial"
                if playwright_ready or browser_present
                else "missing"
            ),
            "reason": (
                "Shell or local browser presence was detected, but host-level browser control and approval gating still need verification."
                if playwright_ready or browser_present
                else "No local browser route hints were detected from shell or standard macOS app locations."
            ),
        },
    }


def main() -> int:
    commands = {
        "gemini": _probe_command("gemini"),
        "playwright": _probe_command("playwright"),
    }
    apps = _probe_mac_apps()
    env_flags = {
        "GEMINI_API_KEY": bool(os.environ.get("GEMINI_API_KEY")),
        "NANOBANANA_API_KEY": bool(os.environ.get("NANOBANANA_API_KEY")),
    }

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cwd": os.getcwd(),
        "host": {
            "platform": platform.platform(),
            "python": sys.version.split()[0],
            "shell": os.environ.get("SHELL"),
        },
        "commands": commands,
        "mac_apps": apps,
        "env": env_flags,
        "route_readiness": _route_readiness(commands, apps),
        "notes": [
            "Command presence is not the same as host tool availability.",
            "Browser route readiness still depends on MCP or app-control access in the current host.",
            "Gemini CLI image generation must be verified separately from basic shell availability.",
        ],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

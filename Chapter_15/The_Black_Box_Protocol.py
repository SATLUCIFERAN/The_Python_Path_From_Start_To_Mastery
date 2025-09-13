import typer
from pathlib import Path
from datetime import datetime, timedelta
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.traceback import install
from dotenv import dotenv_values
import yaml
import time
import tempfile
import shutil
import os

import json 
import sys 

# This is a powerful safety feature for clear error reports.
install()

console = Console()

# --- Step 1: Establish the Droid's Chain of Command ---

defaults = {
    'since_days': 7,
    'out_path': 'report.csv',
    'keep': 3,
    'log_path': 'run_log.jsonl' 
}

env_config = dotenv_values(".env")

yaml_config = {}
if Path("config.yaml").exists():
    with open("config.yaml", "r") as f:
        yaml_config = yaml.safe_load(f) or {}

config = defaults.copy()
config.update({k.lower(): v for k, v in env_config.items()})
mission = yaml_config.get("mission", {})
if "since" in mission:
    config["since_days"] = mission["since"]
if "out" in mission:
    config["out_path"] = mission["out"]
if "keep" in mission:
    config["keep"] = mission["keep"]
if "log" in mission: # New config for log path
    config["log_path"] = mission["log"]

def rotate_reports(path: Path, keep_count: int):
    """
    This function handles the report rotation protocol,
    keeping only the most recent reports.
    """
    console.print(f"[cyan]Initiating file rotation protocol...[/cyan]")
    # Get all files that match the output pattern
    files = list(path.parent.glob(f"{path.stem}*"))
    
    # Sort files by creation time (most recent first)
    files.sort(key=os.path.getmtime, reverse=True)

    # Delete any files that exceed the `keep_count`
    for old_file in files[keep_count:]:
        console.print(f"[yellow]  Deleting old report: {old_file}[/yellow]")
        os.remove(old_file)

def log_run(status: str, message: str, metadata: dict, log_path: Path):  
    run_log = {
        "timestamp": datetime.now().isoformat(),
        "status": status,
        "message": message,
        "metadata": metadata,
    }
    try:
        with open(log_path, "a") as f:
            f.write(json.dumps(run_log) + '\n')
        console.print(f"[bold green]Run log saved to: {log_path}[/bold green]")
    except Exception as e:
        # A last resort to log errors if the log path itself is bad
        console.print(f"[bold red]CRITICAL: Could not write to log path {log_path}. Error: {e}[/bold red]")


# A powerful Typer command to run the droid.

def main(
    since: int = typer.Option(
        int(config.get('since_days', 7)),
        "--since",
        "-s",
        help="The number of days of data to process.",
    ),
    out: str = typer.Option(
        config.get('out_path', 'report.csv'),
        "--out",
        "-o",
        help="The path to save the final report.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-d",
        help="Simulate the mission without creating or modifying files.",
    ),
    keep: int = typer.Option(
        int(config.get('keep', 3)),
        "--keep",
        "-k",
        help="The number of reports to keep during rotation.",
    ),
    log: str = typer.Option(
        config.get('log_path', 'run_log.jsonl'), # New command-line option for log path
        "--log",
        "-l",
        help="The path to save the run log."
    ),
):
    
    """
    I am a Data Courier droid, here to process data and deliver reports.
    """
    console.print(f"[bold green]Master, I will begin my mission with the following chain of command:[/bold green]")
    console.print(f"  [bold]Hardwired Default:[/bold] Since={defaults['since_days']}, Out={defaults['out_path']}, Keep={defaults['keep']}, Log={defaults['log_path']}")
    console.print(f"  [bold]Env Orders:[/bold] {env_config}")
    console.print(f"  [bold]YAML Briefing:[/bold] {yaml_config}")
    console.print(f"  [bold]Final Orders:[/bold] Since={since}, Out={out}, Dry Run={dry_run}, Keep={keep}, Log={log}\n")

    log_metadata = {
        "since": since,
        "out": out,
        "dry_run": dry_run,
        "keep": keep,
    }
    
    if dry_run:
        console.print("[yellow]Activating Dry Run Protocol...[/yellow]")
        console.print(f"I would process data from [bold]{(datetime.now() - timedelta(days=since)).strftime('%Y-%m-%d')}[/bold]"
                        f" to [bold]{datetime.now().strftime('%Y-%m-%d')}[/bold].")
        console.print(f"I would save the report to: [bold]{out}[/bold].")
        console.print(f"I would keep [bold]{keep}[/bold] reports during rotation.")
        log_run(
            status="SUCCESS",
            message="Mission succeeded.",
            metadata=log_metadata,
            log_path=Path(log)
        )
        sys.exit(0)

    # All mission logic is now contained within this block
    exit_code = 1 # Start in a failure state
    try:
        # --- Step 2: Mission Execution Protocol ---
        console.print("[green]Activating Mission Mode...[/green]")
        total_tasks = 100
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing Data...", total=total_tasks)
            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.01)

        # --- Step 3: Droid delivers the report safely using atomic writes and rotation ---
        out_path = Path(out)
        console.print(f"[green]Saving report to: [bold]{out_path}[/bold]...")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Create a temporary file in the same directory for an atomic write
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=out_path.parent) as tmp_file:
            tmp_path = Path(tmp_file.name)
            tmp_file.write(f"Mission Report\n")
            tmp_file.write(f"Data processed from {(datetime.now() - timedelta(days=since)).strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}\n")
            tmp_file.write("Status: Complete")
        shutil.move(tmp_path, out_path)

        # The droid now rotates the files after a successful delivery
        rotate_reports(out_path, keep)

        table = Table(title="Mission Status Report")
        table.add_column("Metric", style="bold")
        table.add_column("Value")
        table.add_row("Status", "[green]Success[/green]")
        table.add_row("Data Processed", f"{since} days")
        table.add_row("Report Path", str(out_path))

        console.print(table)
        console.print("[green]Mission complete![/green]")
        
        # Only on complete, successful execution is the exit code changed
        exit_code = 0 

    except Exception as e:
        console.print(f"[red]Mission failed due to a system error: {e}[/red]")
        console.print("[red]Mission aborted.[/red]")
        # exit_code remains 1 from the start of the block

    finally:
        # The finally block now simply reports the final exit_code
        log_run(
            status="SUCCESS" if exit_code == 0 else "FAILURE",
            message=f"Mission {'succeeded' if exit_code == 0 else 'failed'}.",
            metadata=log_metadata,
            log_path=Path(log)
        )
        sys.exit(exit_code) 

if __name__ == "__main__":
    typer.run(main)

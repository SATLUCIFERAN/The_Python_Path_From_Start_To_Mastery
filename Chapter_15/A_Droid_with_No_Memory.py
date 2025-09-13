
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
import os # New library to get file modification times

# This is a powerful safety feature for clear error reports.
install()

console = Console()

# --- Step 1: Establish the Droid's Chain of Command ---
defaults = {
    'since_days': 7,
    'out_path': 'report.csv',
    'keep': 3,
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
):
    """
    I am a Data Courier droid, here to process data and deliver reports.
    """
    console.print(f"[bold green]Master, I will begin my mission with the following chain of command:[/bold green]")
    console.print(f"  [bold]Hardwired Default:[/bold] Since={defaults['since_days']}, Out={defaults['out_path']}, Keep={defaults['keep']}")
    console.print(f"  [bold]Env Orders:[/bold] {env_config}")
    console.print(f"  [bold]YAML Briefing:[/bold] {yaml_config}")
    console.print(f"  [bold]Final Orders:[/bold] Since={since}, Out={out}, Dry Run={dry_run}, Keep={keep}\n")

    # --- Step 2: Mission Execution Protocol ---
    end_date = datetime.now()
    start_date = end_date - timedelta(days=since)

    if dry_run:
        console.print("[yellow]Activating Dry Run Protocol...[/yellow]")
        console.print(f"I would process data from [bold]{start_date.strftime('%Y-%m-%d')}[/bold]"
                      f" to [bold]{end_date.strftime('%Y-%m-%d')}[/bold].")
        console.print(f"I would save the report to: [bold]{out}[/bold].")
        console.print(f"I would keep [bold]{keep}[/bold] reports during rotation.")
        return

    console.print("[green]Activating Mission Mode...[/green]")
    total_tasks = 100
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing Data...", total=total_tasks)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.01)

    # --- Step 3: Droid delivers the report safely using atomic writes and rotation ---
    out_path = Path(out)

    try:
        console.print(f"[green]Saving report to: [bold]{out_path}[/bold]...")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Create a temporary file in the same directory for an atomic write
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=out_path.parent) as tmp_file:
            tmp_path = Path(tmp_file.name)
            tmp_file.write(f"Mission Report\n")
            tmp_file.write(f"Data processed from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n")
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

    except Exception as e:
        console.print(f"[red]Mission failed due to a system error: {e}[/red]")
        console.print("[red]Mission aborted.[/red]")

if __name__ == "__main__":
    typer.run(main)

    

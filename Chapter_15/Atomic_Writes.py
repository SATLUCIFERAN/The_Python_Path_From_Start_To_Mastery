
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
import tempfile # New library to create temporary files
import shutil # New library to move files

# This is a powerful safety feature for clear error reports.
install()

console = Console()

# --- Step 1: Establish the Droid's Chain of Command ---
# The droid will consult its orders in this specific order of priority.

# 1. Hardwired defaults (lowest priority)
defaults = {
    'since_days': 7,
    'out_path': 'report.csv'
}

# 2. Standing orders from the .env file
env_config = dotenv_values(".env")

# 3. Mission briefing from the config.yaml file (new step)
yaml_config = {}
if Path("config.yaml").exists():
    with open("config.yaml", "r") as f:
        yaml_config = yaml.safe_load(f) or {}

# 4. Final configuration: Merge all orders
config = defaults.copy()
config.update({k.lower(): v for k, v in env_config.items()})
mission = yaml_config.get("mission", {})
if "since" in mission:
    config["since_days"] = mission["since"]
if "out" in mission:
    config["out_path"] = mission["out"]

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
):
    """
    I am a Data Courier droid, here to process data and deliver reports.
    """
    console.print(f"[bold green]Master, I will begin my mission with the following chain of command:[/bold green]")
    console.print(f"  [bold]Hardwired Default:[/bold] Since={defaults['since_days']}, Out={defaults['out_path']}")
    console.print(f"  [bold]Env Orders:[/bold] {env_config}")
    console.print(f"  [bold]YAML Briefing:[/bold] {yaml_config}")
    console.print(f"  [bold]Final Orders:[/bold] Since={since}, Out={out}, Dry Run={dry_run}\n")

    # --- Step 2: Mission Execution Protocol ---
    end_date = datetime.now()
    start_date = end_date - timedelta(days=since)

    # Droid performs a critical safety check for a dry run
    if dry_run:
        console.print("[yellow]Activating Dry Run Protocol...[/yellow]")
        console.print(f"I would process data from [bold]{start_date.strftime('%Y-%m-%d')}[/bold]"
                      f" to [bold]{end_date.strftime('%Y-%m-%d')}[/bold].")
        console.print(f"I would save the report to: [bold]{out}[/bold].")
        return

    # If not a dry run, the droid activates its primary systems
    console.print("[green]Activating Mission Mode...[/green]")

    total_tasks = 100
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing Data...", total=total_tasks)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.01)

    # --- Step 3: Droid delivers the report safely using atomic writes ---
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

        # Atomically replace the final file with the temporary one
        # This is a critical safety step
        shutil.move(tmp_path, out_path)

        # After a successful mission, the droid reports back
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
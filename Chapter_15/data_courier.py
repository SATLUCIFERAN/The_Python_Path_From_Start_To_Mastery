
import typer
from pathlib import Path
from datetime import datetime, timedelta
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.traceback import install
from dotenv import dotenv_values
import time

# Install a pretty traceback handler.
install()

# Initialize a console for pretty output
console = Console()

# Load standing orders from the .env file
config = dotenv_values(".env")

def main(
    since: int = typer.Option(
        int(config.get("SINCE_DAYS", 7)),
        "--since",
        "-s",
        help="The number of days to process data for (e.g., --since 7 for the last week)."
    ),
    out: str = typer.Option(
        config.get("OUT_PATH", "report.csv"),
        "--out",
        "-o",
        help="The path to save the final report to (e.g., --out reports/daily.csv)."
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-d",
        help="Test the mission without performing any actual actions."
    )
):
  
    """
    I am a Data Courier droid. I collect, process, and deliver data reports.
    """
    

    end_date = datetime.now()
    start_date = end_date - timedelta(days=since)
    
    if dry_run:
        console.print("[yellow]Activating Dry Run Mode...[/yellow]")
        console.print("I would process data from "
                      f"[bold]{start_date.strftime('%Y-%m-%d')}[/bold]" 
                      f"(to [bold]{end_date.strftime('%Y-%m-%d')}[/bold].")
        console.print("I would save the report to the following path:" 
                      f"([bold]{out}[/bold].")
        console.print("[yellow]Dry Run complete. No files were created.[/yellow]")
        return
        
    console.print("[green]Activating Mission Mode...[/green]")    
    with Progress(console=console) as progress:
        task = progress.add_task("[green]Collecting data...[/green]", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.01)

    console.print(f"Saving data to [bold]{out}[/bold]...")    
    try:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w") as f:
            f.write(f"Report from {start_date.strftime('%Y-%m-%d')}" 
                    f"to {end_date.strftime('%Y-%m-%d')}\n")
            f.write("Data,Value\n")
            f.write("Some,Data\n")

        table = Table(title="Mission Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Mission Status", "[green]SUCCESS[/green]")
        table.add_row("Data Processed", "100 records")
        table.add_row("Timeframe", f"{since} days")
        table.add_row("Output Path", out)
        
        console.print("\n")
        console.print(table)
        console.print("\n[green]Mission complete! Data report delivered.[/green]")

    except Exception as e:
        console.print(f"[red] An error occurred during file delivery: {e}[/red]")
        typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(main)

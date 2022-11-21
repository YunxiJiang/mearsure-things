import typer
import json
import os


app = typer.Typer()

@app.command("add")
def add_things(name: str, time: float):
    """Add things you want to do

    Args:\n
        name (str): The name of things \n
        time (float): the time you want to use for a day
    """
    data = {"name": name, "time": time, "start_time": 0.0}
    data_json = json.dumps(data)

    if (os.path.exists('data.json')):
        with open('data.json','a') as outfile:
            outfile.write(data_json)
            outfile.close()
    else:
        with open('data.json','x') as outfile:
            outfile.close()


    print(f'Add {name} successful. \nThe time to do this is {time}')

@app.command()
def delete_things(name: str):
    """Delete things you already add

    Args:\n
        name (str): The name of things
    """
    print(f'Delete {name} successful.')

@app.command()
def start(name: str):
    """Start one thing and time will start caculating

    Args:\n
        name (str): The name of things
    """
    print(f'Start {name} successful.')

@app.command()
def end(name: str):
    """Stop one thing which you already started and time will stop caculating

    Args:\n
        name (str): The name of things
    """
    print(f'Stop {name} successful.')


@app.command()
def show():
    """Show all the things you want to do
    """
    return True


@app.command()
def graphic():
    """Show graphic of history of doing things
    """
    return True

if __name__ == "__main__":
    app()
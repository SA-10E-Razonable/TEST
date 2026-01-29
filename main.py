from pyscript import document

def show_results(event):
    try:
        energy = float(document.getElementById("bar-energy").value)
        tempo = float(document.getElementById("bar-tempo").value)
    except ValueError:
        document.getElementById("view-results").innerText = "Please enter valid numbers!"
        return

    if energy < 0 or energy > 100 or tempo < 0 or tempo > 100:
        document.getElementById("view-results").innerText = "Values must be between 0 and 100!"
        return

    beat = (energy + tempo) / 2

    if beat <= 40:
        style = "Chill / Lo-Fi 🎧"
    elif beat <= 70:
        style = "Pop 🎵"
    elif beat <= 90:
        style = "Rock 🔥"
    else:
        style = "EDM ⚡"

    document.getElementById("view-results").innerText = f"You match the beat: {style}"

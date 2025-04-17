# code und pseudocode zu 100% KI generiert

# Definition der Funktion zur Visualisierung der Türme
def visualisiere_tuerme(tuerme):
    # Bestimme die maximale Höhe aller Türme
    max_hoehe = max(len(turm) for turm in tuerme.values())
    
    # Durchlaufe die Türme von oben nach unten
    for hoehe in range(max_hoehe - 1, -1, -1):
        # Gehe durch alle drei Stäbe (A, B, C)
        for stab in ['A', 'B', 'C']:
            # Prüfe ob auf dieser Höhe eine Scheibe existiert
            if hoehe < len(tuerme[stab]):
                # Zeige Scheibe als Reihe von '#' Zeichen an
                # Die Anzahl der '#' entspricht der Scheibengröße
                print(f"  {'#' * tuerme[stab][hoehe]}  ", end='')
            else:
                # Wenn keine Scheibe vorhanden ist, zeige nur den Stab '|'
                print("  |  ", end='')
        # Gehe zur nächsten Zeile für die nächste Höhe
        print()
    # Zeichne eine Trennlinie unter den Türmen
    print("-" * 35)
    # Beschrifte die Türme
    print("  A     B     C  ")
    print()

def hanoi_mit_visual(n, quelle, ziel, hilfe):
    # Initialisierung der Türme: Alle Scheiben beginnen auf Turm A
    tuerme = {
        'A': list(range(n, 0, -1)),  # Scheiben absteigend nach Größe
        'B': [],                      # Hilfsturm ist leer
        'C': []                       # Zielturm ist leer
    }
    
    def bewege_scheibe(von, nach):
        # Nimm die oberste Scheibe vom Quellturm
        scheibe = tuerme[von].pop()
        # Lege sie auf den Zielturm
        tuerme[nach].append(scheibe)
        # Zeige die Bewegung an
        print(f"\nBewege Scheibe {scheibe} von {von} nach {nach}")
        # Visualisiere den aktuellen Zustand
        visualisiere_tuerme(tuerme)
    
    # Zeige die Ausgangssituation
    print("\nStartposition:")
    visualisiere_tuerme(tuerme)
    
    # Iterative Lösung mit Stack
    bewegungen = []
    bewegungen.append((n, quelle, ziel, hilfe))
    
    while bewegungen:
        # Hole die nächste Bewegung vom Stack:
        # scheiben: Anzahl der zu bewegenden Scheiben
        # q: Quellturm
        # z: Zielturm  
        # h: Hilfsturm
        scheiben, q, z, h = bewegungen.pop()
        
        if scheiben == 1:
            bewege_scheibe(q, z)
        else:
            bewegungen.append((scheiben-1, h, z, q))
            bewegungen.append((1, q, z, h))
            bewegungen.append((scheiben-1, q, h, z))

# Hauptprogramm mit Visualisierung
if __name__ == "__main__":
    # Setze die Anzahl der Scheiben für die visuelle Demonstration
    anzahl_scheiben = 6
    print(f"\nLösung für {anzahl_scheiben} Scheiben mit Visualisierung:")
    # Starte die visuelle Demonstration
    hanoi_mit_visual(anzahl_scheiben, 'A', 'C', 'B')

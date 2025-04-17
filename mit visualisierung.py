
def hanoi(n, quelle, ziel, hilfe):
    # Basisfall: Wenn nur eine Scheibe zu bewegen ist
    if n == 1:
        # Gib die Bewegung der kleinsten Scheibe (1) aus
        print(f"Bewege Scheibe 1 von {quelle} nach {ziel}")
        # Beende die Rekursion für n=1
        return
    
    # Bewege n-1 Scheiben von Quelle auf Hilfsturm
    hanoi(n-1, quelle, hilfe, ziel)
    # Bewege die größte Scheibe n von Quelle zum Ziel
    print(f"Bewege Scheibe {n} von {quelle} nach {ziel}")
    # Bewege die n-1 Scheiben vom Hilfsturm zum Ziel
    hanoi(n-1, hilfe, ziel, quelle)

def main():
    # Anzahl der Scheiben für das Spiel festlegen
    anzahl_scheiben = 6
    
    # Ausgabe der Startmeldung
    print(f"\nLösung für {anzahl_scheiben} Scheiben:")
    
    # Starte die Berechnung mit:
    # - Quelle 'A': Startturm
    # - Ziel 'C': Zielturm  
    # - Hilfe 'B': Hilfsturm für Zwischenschritte
    hanoi(anzahl_scheiben, 'A', 'C', 'B')

if __name__ == "__main__":
    # Starte das Hauptprogramm
    main()
    
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
        
        def hanoi_rekursiv(n, quelle, ziel, hilfe):
            # Basisfall: Bewege eine einzelne Scheibe direkt
            if n == 1:
                bewege_scheibe(quelle, ziel)
                return
            # Rekursive Fälle:
            # 1. Bewege n-1 Scheiben auf den Hilfsturm
            hanoi_rekursiv(n-1, quelle, hilfe, ziel)
            # 2. Bewege die größte Scheibe zum Ziel
            bewege_scheibe(quelle, ziel)
            # 3. Bewege die n-1 Scheiben vom Hilfsturm zum Ziel
            hanoi_rekursiv(n-1, hilfe, ziel, quelle)
        
        # Zeige die Ausgangssituation
        print("\nStartposition:")
        visualisiere_tuerme(tuerme)
        # Starte die rekursive Lösung
        hanoi_rekursiv(n, quelle, ziel, hilfe)

    # Hauptprogramm mit Visualisierung
    if __name__ == "__main__":
        # Setze die Anzahl der Scheiben für die visuelle Demonstration
        anzahl_scheiben = 6
        print(f"\nLösung für {anzahl_scheiben} Scheiben mit Visualisierung:")
        # Starte die visuelle Demonstration
        hanoi_mit_visual(anzahl_scheiben, 'A', 'C', 'B')

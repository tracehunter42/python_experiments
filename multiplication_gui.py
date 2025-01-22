import tkinter as tk
import random

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Malá násobilka")
        self.root.geometry("500x400")
        self.root.configure(bg="#2b2b2b")  # Moderné tmavé pozadie
        self.spravne_odpovede = 0
        self.pocet_prikladov = random.randint(1, 10)
        self.current_priklad = None
        self.current_index = 0

        # GUI prvky
        sklonovanie = self.get_sklonovanie(self.pocet_prikladov)
        self.info_label = tk.Label(root, text=f"Budeš riešiť {self.pocet_prikladov} {sklonovanie}.",
                                   bg="#2b2b2b", fg="#f0a500", font=("Arial", 16, "bold"))
        self.info_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", bg="#2b2b2b", fg="#ffffff", font=("Arial", 14))
        self.question_label.pack(pady=5)

        self.answer_entry = tk.Entry(root, font=("Arial", 14), bg="#444444", fg="#ffffff", insertbackground="#ffffff")
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Odoslať", command=self.submit_answer,
                                       bg="#f0a500", fg="#2b2b2b", font=("Arial", 14, "bold"), relief="flat")
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", bg="#2b2b2b", fg="#00ff00", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.result_label = tk.Label(root, text="", bg="#2b2b2b", fg="#ffffff", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.vytvor_priklad()

    def get_sklonovanie(self, number):
        if number == 1:
            return "príklad"
        elif 2 <= number <= 4:
            return "príklady"
        else:
            return "príkladov"

    def vytvor_priklad(self):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        self.current_priklad = (a, b, a * b)
        self.question_label.config(text=f"Koľko je {a} * {b}?")
        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        try:
            odpoved = int(self.answer_entry.get())
        except ValueError:
            self.feedback_label.config(text="Zadaj platné číslo!", fg="#ff0000")
            return

        if odpoved == self.current_priklad[2]:
            self.feedback_label.config(text="Správne!", fg="#00ff00")
            self.spravne_odpovede += 1
        else:
            self.feedback_label.config(text=f"Chyba! Správna odpoveď je {self.current_priklad[2]}.", fg="#ff0000")

        self.current_index += 1
        if self.current_index < self.pocet_prikladov:
            self.vytvor_priklad()
        else:
            self.koniec_hry()

    def koniec_hry(self):
        percenta = (self.spravne_odpovede / self.pocet_prikladov) * 100
        result_text = f"Získal si {round(percenta)}%.\n"

        if percenta >= 90:
            result_text += "Super výsledok, získavaš odmenu!\n"
            odmeny = [
                "   __|__\n   --o--o--(_)--o--o--\n ✈  Boeing 747",
                "    __o\n  _ \\<_\n (_)>(_)\nDanko na bicykli :-)",
                "ʕ·͡ᴥ·ʔ\nbrum brum"
            ]
            result_text += random.choice(odmeny)
        else:
            result_text += "To nevadí, skús to znova. ¯\_(ツ)_/¯"

        self.result_label.config(text=result_text)
        self.submit_button.config(state=tk.DISABLED)
        self.answer_entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
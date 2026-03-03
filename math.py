import statistics

class BasicStatisticalMetrics:
    def __init__(self, data):
        """
        Αρχικοποίηση της κλάσης με μια λίστα αριθμών.
        Αν η λίστα είναι άδεια, εγείρει ένα σφάλμα.
        """
        if not data:
            raise ValueError("Η λίστα δεν μπορεί να είναι άδεια.")
        self.data = data

    def calculate_mean(self):
        """Υπολογισμός του Μέσου Όρου (Mean)"""
        return sum(self.data) / len(self.data)

    def calculate_std_deviation(self):
        """Υπολογισμός της Τυπικής Απόκλισης (Standard Deviation)"""
        return statistics.stdev(self.data)

    def calculate_median(self):
        """Υπολογισμός της Διαμέσου (Median)"""
        return statistics.median(self.data)

    def display_all(self):
        """Εμφάνιση όλων των αποτελεσμάτων συγκεντρωτικά"""
        print(f"Δεδομένα: {self.data}")
        print(f"Μέσος Όρος: {self.calculate_mean():.2f}")
        print(f"Τυπική Απόκλιση: {self.calculate_std_deviation():.2f}")
        print(f"Διάμεσος: {self.calculate_median():.2f}")

# --- Παράδειγμα Χρήσης ---
numbers = [2, -1, 5, 1, 1, 34, 37]

# Δημιουργία αντικειμένου της κλάσης
stats = BasicStatisticalMetrics(numbers)

# Εκτύπωση των αποτελεσμάτων
stats.display_all()
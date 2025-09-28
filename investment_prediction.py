import matplotlib.pyplot as plt
import numpy as np

# Suma inițială
initial_investment = 15000

# Dobânzi anuale
deposit_interest_rate = 0.02
fidelis_coupon_rate = 0.065

# Scenarii FIDELIS: [price change, label]
fidelis_scenarios = [
    (1.00, "Dobânzi constante (preț 100%)"),
    (1.03, "Dobânzi scad (preț 103%)"),
    (0.95, "Dobânzi cresc (preț 95%)"),
]

# Calcule pentru fiecare scenariu
results = []
for price_factor, label in fidelis_scenarios:
    coupon = initial_investment * fidelis_coupon_rate
    redemption_value = initial_investment * price_factor
    total_return = coupon + redemption_value
    roi = (total_return - initial_investment) / initial_investment * 100
    results.append((label, total_return, roi))

# Depozit bancar
deposit_interest = initial_investment * deposit_interest_rate
deposit_tax = deposit_interest * 0.10
deposit_net = initial_investment + (deposit_interest - deposit_tax)
deposit_roi = (deposit_net - initial_investment) / initial_investment * 100

# Adăugăm și depozitul la rezultate
results.append(("Depozit bancar 2%", deposit_net, deposit_roi))

# Sortare după ROI descrescător
results.sort(key=lambda x: x[2], reverse=True)

# Pregătim datele pentru grafic
labels = [r[0] for r in results]
values = [r[1] for r in results]
rois = [r[2] for r in results]

# Grafic
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color='skyblue')
plt.axhline(y=initial_investment, color='gray', linestyle='--', label='Investiție inițială')
plt.ylabel("Valoare finală (€)")
plt.title("Comparatie: Investiție FIDELIS vs. Depozit bancar (1 an)")

# Etichete ROI deasupra barelor
for bar, roi in zip(bars, rois):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 50, f"{roi:.1f}%", 
             ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=15)
plt.tight_layout()
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Comparație între RO2610AE (2026) și FIDELIS 6.5% (2035)

import matplotlib.pyplot as plt
import numpy as np

# Suma investită
investment = 15000

# RO2610AE (2026) - scurt
ro2610_price_dirty = 99.72
ro2610_coupon_rate = 0.016
ro2610_years = 1.16  # ~14 luni până la maturitate
ro2610_titles = investment // ro2610_price_dirty
ro2610_total_coupons = ro2610_titles * ro2610_coupon_rate * 100 * ro2610_years
ro2610_redemption = ro2610_titles * 100
ro2610_total_return = ro2610_total_coupons + ro2610_redemption
ro2610_roi = (ro2610_total_return - investment) / investment * 100

# FIDELIS 6.5% (2035) - lung, dar vândut în 2026
fidelis_coupon_rate = 0.065
fidelis_dirty_price = 100  # presupunem prețul e stabil
fidelis_titles = investment // fidelis_dirty_price
fidelis_coupon_2026 = fidelis_titles * 100 * fidelis_coupon_rate
# scenarii de preț vânzare:
fidelis_prices = [0.95, 1.00, 1.03]
fidelis_results = []

for price_factor in fidelis_prices:
    redemption = fidelis_titles * 100 * price_factor
    total = redemption + fidelis_coupon_2026
    roi = (total - investment) / investment * 100
    fidelis_results.append((price_factor, total, roi))

# Pregătire grafic
labels = ['RO2610AE (2026)']
values = [ro2610_total_return]
rois = [ro2610_roi]

for factor, total, roi in fidelis_results:
    label = f'FIDELIS 6.5% (vândut la {int(factor*100)}%)'
    labels.append(label)
    values.append(total)
    rois.append(roi)

# Grafic
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color='lightblue')
plt.axhline(y=investment, color='gray', linestyle='--', label='Investiție inițială')
plt.ylabel("Valoare finală estimată (€)")
plt.title("Comparație: FIDELIS 6.5% vs. RO2610AE (2026) — investiție 15.000€")

for bar, roi in zip(bars, rois):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 40, f"{roi:.1f}%", 
             ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=15)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()

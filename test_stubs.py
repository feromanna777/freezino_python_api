# test_stubs.py
import requests

BASE = "http://localhost:3000"

# GET-эндпоинты, которые должны вернуть 200 + envelope
get_endpoints = [
    "/api/shop/items",
    "/api/shop/my-items",
    "/api/games/roulette/recent",
    "/api/games/sessions",
    "/api/loans",
    "/api/loans/summary",
    "/api/loans/bankruptcy-check",
    "/api/stats/casino",
    "/api/stats/countries",
    "/api/user/transactions",
    "/api/user/items",
]

# POST-эндпоинты, которые должны вернуть 501
post_endpoints = [
    "/api/auth/refresh",
    "/api/auth/logout",
    "/api/shop/buy/1",
    "/api/shop/sell/1",
    "/api/games/roulette/bet",
    "/api/games/slots/spin",
    "/api/loans/take",
    "/api/loans/repay/1",
    "/api/contact",
    "/api/dev/seed",
]

print("🔍 Тестируем GET-заглушки...")
for ep in get_endpoints:
    r = requests.get(f"{BASE}{ep}")
    status = "✅" if r.status_code == 200 and r.json().get("success") is True else "❌"
    print(f"{status} {ep} → {r.status_code}")

print("\n🔍 Тестируем POST-заглушки...")
for ep in post_endpoints:
    r = requests.post(f"{BASE}{ep}")
    status = "✅" if r.status_code == 501 else "❌"
    print(f"{status} {ep} → {r.status_code}")

print("\n🔍 Спецслучай: /api/stats/countries/US → должен быть 404")
r = requests.get(f"{BASE}/api/stats/countries/US")
status = "✅" if r.status_code == 404 else "❌"
print(f"{status} /api/stats/countries/US → {r.status_code}")
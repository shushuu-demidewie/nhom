import requests

print("=== BAI TAP 5.1: API GITHUB REPO ===")
url_github = "https://api.github.com/repos/python/cpython"
try:
    response_gh = requests.get(url_github, timeout=10)
    if response_gh.status_code == 200:
        du_lieu_gh = response_gh.json()
        print("Ten repository:", du_lieu_gh["full_name"])
        print("So luot gan sao (stars):", du_lieu_gh["stargazers_count"])
        print("Ngon ngu chinh:", du_lieu_gh["language"])
    else:
        print("Goi API that bai, ma loi:", response_gh.status_code)
except Exception as e:
    print("Loi ket noi den GitHub API:", e)

print("\n=== BAI TAP 5.2: API TY GIA NGOAI TE ===")
url_exchange = "https://open.er-api.com/v6/latest/USD"
try:
    response_ex = requests.get(url_exchange, timeout=10)
    if response_ex.status_code == 200:
        du_lieu_ex = response_ex.json()
        ty_gia_vnd = du_lieu_ex["rates"]["VND"]
        print(f"1 USD = {ty_gia_vnd:,.0f} VND")
    else:
        print("Khong lay duoc ty gia, ma loi:", response_ex.status_code)
except Exception as e:
    print("Loi ket noi den Ty Gia API:", e)
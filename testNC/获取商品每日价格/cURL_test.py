import requests

headers = {
    'authority': 'detail.tmall.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'lid=%E5%8C%96%E7%BE%BD%E8%80%8C%E8%92%99; enc=NCb7VYT8Mx8Z%2BOsS77I0lK886vcBEz%2FJcauTnwBXaFa0K6gh%2B8b%2B0LbRYMfxuGvUb362ZaBgBWvVr4lC6guaIA%3D%3D; _m_h5_tk=99e66ff727f1b128c207535caa7874b4_1644924145944; _m_h5_tk_enc=b01050f69f5a79975790188ccb058f68; cna=An96Ggi7UkgCAbcw8TW79zC4; pnm_cku822=098%23E1hvYvvUvbpvUvCkvvvvvjiWR25vgjtURscWljljPmP9sjnbnLs9sjiEnLFW0jYbRvhvChCvvvvRvpvhvv2MMQ9Cvh1vk6IvItxkh7ERiNowecH2fCuYiLUpwh%2BFp%2B0xhCDAo2Ec6aZtn0vHVA5OaXTOJhxYpExreBIaWoyZD76XV16kwZ2vACyaayHApd2XKvhv8hCvvHQvvhCvphvwv9vvp%2FHvpCQmvvChNhCvjvUvvhRAphvwv9vvpq8IvpvUphvhMpPNjK8UvpvVpyUU2EQwvvhvCyCCvvvvv8OCvvBvpvpZ; isg=BMnJJFwXz3aAXbD-4iUIRyV52PMjFr1IrMZDaGs-KrDvsunEsWQpGLej8BYE6lWA; l=eBIE6fG4gdn_Gh6xBOfwlurza77OcIRAguPzaNbMiOCPOUfB5wLVW6cECl86CnGVh6c6-38r7aOkBeYBc_C-nxv9N0m65Tkmn; tfstk=cfgCBd2PIY3ZvpxP8XOw8Izx9UURCuCbNHwnO07qiQReKt-bIa1mAZyfsEilezP81',
}

params = (
    ('spm', 'a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA'),
    ('id', '606744628264'),
    ('skuId', '4430618975202'),
)

response = requests.get('https://detail.tmall.com/item.htm', headers=headers, params=params)

print(response.text)
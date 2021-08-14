from amazon_buy_bot import *
true = True
false = False
list_of_cookies = [
{
    "domain": ".amazon.in",
    "expirationDate": 1644925588.404523,
    "hostOnly": false,
    "httpOnly": false,
    "name": "i18n-prefs",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "INR",
    "id": 1
}]
#please replace the above sample cookies with your cookies, can see below link of how to fetch cookies
product_link="https://www.amazon.in/Boat-Airdopes-171-Functionality-Resistance/dp/B086WN6N4G/ref=sr_1_14_mod_primary_lightning_deal?crid=1YHOUOZCKZVNV&dchild=1&keywords=earbuds+wireless&qid=1613389628&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A14CZOWI0VEHLG&sprefix=earb%2Caps%2C850&sr=8-14"
amazon.login_cookie(cookies=list_of_cookies)
amazon.buy(product_url=product_link)
amazon.select_payment_method(payment_method='Punjab National Bank Debit Card')
amazon.fill_cvv(cvv='123')
amazon.place_order()

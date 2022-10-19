const userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};


userCart["lastname"] = "Smith"
userCart.prices.pear = 1.17 * 0.2
//userCart["prices"["pear"]] = 1.17 * 0.2

let userWant = prompt("Which fruit you want ?") //.toLowCase()
console.log(userCart.prices[userWant.toLowerCase()]);


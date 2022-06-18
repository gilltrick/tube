const normalMessage = document.querySelector(".normalMessage")
const showOfferMessageButton = document.querySelector(".showOfferMessageButton")
const offerMessage = document.querySelector(".offerMessage")
const showNormalMessageButton = document.querySelector(".showNormalMessageButton")
const showSendVideoMessageButton = document.querySelector(".showSendVideoMessageButton")
const videoMessage = document.querySelector(".videoMessage")
const _showNormalMessageButton = document.querySelector("._showNormalMessageButton")

document.querySelector(".container").scrollTop = 99999

function ShowOfferMessage(){
    videoMessage.style.display = "none"
    normalMessage.style.display = "none"
	offerMessage.style.display = "block"

}

showOfferMessageButton.addEventListener("click", ShowOfferMessage)

function ShowNormalMessage(){
    videoMessage.style.display = "none"
    offerMessage.style.display = "none"
	normalMessage.style.display = "block"

}

showNormalMessageButton.addEventListener("click", ShowNormalMessage)

function ShowSendVideoMessageButton(){
    offerMessage.style.display = "none"
	normalMessage.style.display = "none"
    videoMessage.style.display = "block"

}

showSendVideoMessageButton.addEventListener("click", ShowSendVideoMessageButton)

function _ShowNormalMessage(){
    videoMessage.style.display = "none"
    offerMessage.style.display = "none"
	normalMessage.style.display = "block"

}

_showNormalMessageButton.addEventListener("click", _ShowNormalMessage)
$(document).ready(function() {

	$("#uploadFile").on("submit", function(event) {

		event.preventDefault();
		var formData = new FormData($("form")[0]);

		$.ajax({

			xhr : function() {

				var xhr = new window.XMLHttpRequest();
				xhr.upload.addEventListener("progress", function(e) {

					if (e.lengthComputable) {

						console.log("Bytes Loaded: " + e.loaded);
						console.log("Total Size: " + e.total);
						console.log("Percentage Uploaded: " + (e.loaded / e.total))
						var percent = Math.round((e.loaded / e.total) * 100);
						$("#progressBar").attr("aria-valuenow", percent).css("width", percent + "%").text(percent + "%");
					}

				});
				return xhr;
			},
			type : "POST",
			url : "/uploadFile",
			data : formData,
			processData : false,
			contentType : false,
			success : function() {
				location.href = "/userAccount";
			},
			error : function(){

				"alert(\"You need to be verified to sell videos!\");location.href = \"/userAccount\";"
			}
		});
	});
});

function getFile() {
	document.getElementById("#uploadFile").click();
  }
  
  function sub(obj) {
	var file = obj.value;
	var fileName = file.split("\\");
	document.getElementById("chooseFileBtn").innerHTML = fileName[fileName.length - 1];
	document.myForm.submit();
	event.preventDefault();
  }

const addVideoContainer = document.querySelector(".addVideoContainer");
const openAddVideoContainer = document.querySelector(".openAddVideoContainer");
const removeVideoContainer = document.querySelector(".removeVideoContainer");
const openRemoveVideoContainer = document.querySelector(".openRemoveVideoContainer");
const editVideoContainer = document.querySelector(".editVideoContainer");
const openEditVideoContainer = document.querySelector(".openEditVideoContainer");
const videoListContainer = document.querySelector(".videoListContainer");
const openVideoListContainer = document.querySelector(".openVideoListContainer");
const closeVideoListContainer = document.querySelector(".closeVideoListContainer");
const removeUserContainer = document.querySelector(".removeUserContainer");
const openRemoveUserContainer = document.querySelector(".openRemoveUserContainer");
const editUserContainer = document.querySelector(".editUserContainer");
const openEditUserContainer = document.querySelector(".openEditUserContainer");
const addVideoSubmitButton = document.querySelector(".addVideoContainer .addToDatabaseBtn")
const infoContainer = document.querySelector(".infoContainer")
const favoritesListContainer = document.querySelector(".favoritesListContainer");
const openFavoritesListContainer = document.querySelector(".openFavoritesListContainer");
const closeFavoritesListContainer = document.querySelector(".closeFavoritesListContainer");
const openPurchasedVideosContainer = document.querySelector(".openPurchasedVideosContainer");
const purchasedVideosListContainer = document.querySelector(".purchasedVideosListContainer");
const closePurchasedVideosListContainer = document.querySelector(".closePurchasedVideosListContainer");
const hiddenDataInputRow = document.querySelector(".hiddenDataInputRow");
const forSaleCheckBox = document.querySelector(".forSale");
const trailerCheckBox = document.querySelector(".trailer");
const freeCheckBox = document.querySelector(".free");
const privateCheckBox = document.querySelector(".privateVideo")


function ForSaleCheckBox(){
	if (forSaleCheckBox.checked == true){//on click it gets checked true before i get to this if

		hiddenDataInputRow.style.display = "flex";
		freeCheckBox.checked = false;
		privateCheckBox.checked = false;
		trailerCheckBox.checked = false;
		return
	}
	hiddenDataInputRow.style.display = "none";

}

forSaleCheckBox.addEventListener("click", ForSaleCheckBox)

function FreeCheckBox(){

	hiddenDataInputRow.style.display = "none";
	privateCheckBox.checked = false;
	forSaleCheckBox.checked = false;
	trailerCheckBox.checked = false;

}

freeCheckBox.addEventListener("click", FreeCheckBox)

function TrailerCheckBox(){

	hiddenDataInputRow.style.display = "none";
	forSaleCheckBox.checked = false;
	privateCheckBox.checked = false;
	freeCheckBox.checked = false;

}

function PrivateCheckBox(){

	hiddenDataInputRow.style.display = "none";
	forSaleCheckBox.checked = false;
	trailerCheckBox.checked = false;
	freeCheckBox.checked = false;
}

privateCheckBox.addEventListener("click", PrivateCheckBox)
trailerCheckBox.addEventListener("click", TrailerCheckBox)

function OpenPurchasedVideosContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	favoritesListContainer.style.display = "none";
	
	purchasedVideosListContainer.style.display = "initial"
}

openPurchasedVideosContainer.addEventListener("click", OpenPurchasedVideosContainer);

function ClosePurchasedVideosListContainer(){
	if (addVideoContainer.style.display != "none"){
		purchasedVideosListContainer.style.display = "none";
		addVideoContainer.style.display = "initial";
	}
	if (removeVideoContainer.style.display != "none"){
		purchasedVideosListContainer.style.display = "none";
		removeVideoContainer.style.display = "initial";
	}
	if (editVideoContainer.style.display != "none"){
		purchasedVideosListContainer.style.display = "none";
		editVideoContainer.style.display = "initial";
	}
	purchasedVideosListContainer.style.display = "none";
}

closePurchasedVideosListContainer.addEventListener("click", ClosePurchasedVideosListContainer);

function OpenAddVideoContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	addVideoContainer.style.display = "initial";
}

openAddVideoContainer.addEventListener("click", OpenAddVideoContainer);

function OpenRemoveVideoContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "initial";
}

openRemoveVideoContainer.addEventListener("click", OpenRemoveVideoContainer);

function OpenEditVideoContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "initial";
}

openEditVideoContainer.addEventListener("click", OpenEditVideoContainer);

function OpenVideoListContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	purchasedVideosListContainer.style.display = "none"
	videoListContainer.style.display = "initial"
}

openVideoListContainer.addEventListener("click", OpenVideoListContainer);

function CloseVideoListContainer(){
	if (addVideoContainer.style.display != "none"){
		videoListContainer.style.display = "none";
		addVideoContainer.style.display = "initial";
	}
	if (removeVideoContainer.style.display != "none"){
		videoListContainer.style.display = "none";
		removeVideoContainer.style.display = "initial";
	}
	if (editVideoContainer.style.display != "none"){
		videoListContainer.style.display = "none";
		editVideoContainer.style.display = "initial";
	}
	videoListContainer.style.display = "none";
}

closeVideoListContainer.addEventListener("click", CloseVideoListContainer)


function OpenRemoveUserContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	editUserContainer.style.display = "none";
	removeUserContainer.style.display = "initial";
}

openRemoveUserContainer.addEventListener("click", OpenRemoveUserContainer);

function OpenEditUserContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "initial";

}

openEditUserContainer.addEventListener("click", OpenEditUserContainer)


function SendAddVideoToDatabaseMessage(){
	infoContainer.style.display = "initial";
	infoContainer.innerHTML = "It will take some time to process the video. You can leave this page and do something different :)";
}

addVideoSubmitButton.addEventListener("click", SendAddVideoToDatabaseMessage)

function CloseInfoContainer(){
	infoContainer.style.display = "none";

}

infoContainer.addEventListener("click", CloseInfoContainer)

function OpenFavoritesListContainer(){
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	favoritesListContainer.style.display = "initial";
}

openFavoritesListContainer.addEventListener("click", OpenFavoritesListContainer);

function CloseFavoritesListContainer(){
	if (addVideoContainer.style.display != "none"){
		favoritesListContainer.style.display = "none";
		addVideoContainer.style.display = "initial";
	}
	if (removeVideoContainer.style.display != "none"){
		favoritesListContainer.style.display = "none";
		removeVideoContainer.style.display = "initial";
	}
	if (editVideoContainer.style.display != "none"){
		favoritesListContainer.style.display = "none";
		editVideoContainer.style.display = "initial";
	}
	favoritesListContainer.style.display = "none";
}

closeFavoritesListContainer.addEventListener("click", CloseFavoritesListContainer);



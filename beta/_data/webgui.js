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
const addUserContainer = document.querySelector(".addUserContainer");
const openAddUserContainer = document.querySelector(".openAddUserContainer");
const removeUserContainer = document.querySelector(".removeUserContainer");
const openRemoveUserContainer = document.querySelector(".openRemoveUserContainer");
const editUserContainer = document.querySelector(".editUserContainer");
const openEditUserContainer = document.querySelector(".openEditUserContainer");
const userListContainer = document.querySelector(".userListContainer");
const openUserListContainer = document.querySelector(".openUserListContainer");
const closeUserListContainer = document.querySelector(".closeUserListContainer");
const addVideoSubmitButton = document.querySelector(".addVideoContainer .addToDatabaseBtn")
const infoContainer = document.querySelector(".infoContainer")
const hiddenDataInputRow = document.querySelector(".hiddenDataInputRow")
const forSaleCheckBox = document.querySelector(".forSale")
const trailerCheckBox = document.querySelector(".trailer")
const freeCheckBox = document.querySelector(".free")
const privateCheckBox = document.querySelector(".privateVideo")


function ForSaleCheckBox(){
	if (forSaleCheckBox.checked == true){//on click it gets checked true before i get to this if

		hiddenDataInputRow.style.display = "flex";
		freeCheckBox.checked = false;
		trailerCheckBox.checked = false;
		privateCheckBox.checked = false;
		return
	}
	hiddenDataInputRow.style.display = "none";

}

forSaleCheckBox.addEventListener("click", ForSaleCheckBox)

function FreeCheckBox(){

	hiddenDataInputRow.style.display = "none";
	forSaleCheckBox.checked = false;
	trailerCheckBox.checked = false;
	privateCheckBox.checked = false;

}

freeCheckBox.addEventListener("click", FreeCheckBox)

function TrailerCheckBox(){

	hiddenDataInputRow.style.display = "none";
	forSaleCheckBox.checked = false;
	freeCheckBox.checked = false;
	privateCheckBox.checked = false;

}

trailerCheckBox.addEventListener("click", TrailerCheckBox)

function PrivateCheckBox(){

	hiddenDataInputRow.style.display = "none";
	forSaleCheckBox.checked = false;
	trailerCheckBox.checked = false;
	freeCheckBox.checked = false;
}

privateCheckBox.addEventListener("click", PrivateCheckBox)

function OpenAddVideoContainer(){
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	addVideoContainer.style.display = "initial";
}

openAddVideoContainer.addEventListener("click", OpenAddVideoContainer);

function OpenRemoveVideoContainer(){
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "initial";
}

openRemoveVideoContainer.addEventListener("click", OpenRemoveVideoContainer);

function OpenEditVideoContainer(){
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "initial";
}

openEditVideoContainer.addEventListener("click", OpenEditVideoContainer);

function OpenVideoListContainer(){
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
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

function OpenAddUserContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	addUserContainer.style.display = "initial";
}

openAddUserContainer.addEventListener("click", OpenAddUserContainer);

function OpenRemoveUserContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	addUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	removeUserContainer.style.display = "initial";
}

openRemoveUserContainer.addEventListener("click", OpenRemoveUserContainer);

function OpenEditUserContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "initial";

}

openEditUserContainer.addEventListener("click", OpenEditUserContainer)

function OpenUserListContainer(){
	addVideoContainer.style.display = "none";
	editVideoContainer.style.display = "none";
	removeVideoContainer.style.display = "none";
	videoListContainer.style.display = "none";
	addUserContainer.style.display = "none";
	removeUserContainer.style.display = "none";
	editUserContainer.style.display = "none";
	userListContainer.style.display = "initial";
}

openUserListContainer.addEventListener("click", OpenUserListContainer)

function CloseUserListContainer(){
	if (addUserContainer.style.display != "none"){
		userListContainer.style.display = "none";
		addUserContainer.style.display = "initial";
		return;
	}
	if (removeUserContainer.style.display != "none"){
		userListContainer.style.display = "none";
		removeUserContainer.style.display = "initial";
		return;
	}
	if (editUserContainer.style.display != "none"){
		userListContainer.style.display = "none";
		editUserContainer.style.display = "initial";
		return;
	}
	userListContainer.style.display = "none";
}

closeUserListContainer.addEventListener("click", CloseUserListContainer)

function SendAddVideoToDatabaseMessage(){
	infoContainer.style.display = "initial";
	infoContainer.innerHTML = "It will take some time to process the video. You can leave this page and do something different :)";
}

addVideoSubmitButton.addEventListener("click", SendAddVideoToDatabaseMessage)

function CloseInfoContainer(){
	infoContainer.style.display = "none";

}

infoContainer.addEventListener("click", CloseInfoContainer)
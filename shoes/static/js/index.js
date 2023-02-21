const icon = document.querySelector(".icon");
const search = document.querySelector(".search");
icon.onclick = function () {
  search.classList.toggle("active");
};

function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
//location
let locationButton = document.getElementById("get-location");
let locationDiv = document.getElementById("location-details");

locationButton.addEventListener("click", () => {
  //Geolocation APU is used to get geographical position of a user and is available inside the navigator object

  if (navigator.geolocation) {
    //returns position (latitude and longitude) or error
    navigator.geolocation.getCurrentPosition(showLocation, checkError);
  } else {
    locationDiv.innerText = "The browser does not support geolocation";
  }
});
//Error Checks
const checkError = (error) => {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      locationDiv.innerText = "Please allow acces to location";
      break;
    case error.POSITION_UNAVAILABLE:
      //usually fired for firefox
      locationDiv.innerText = "Location Information unavailable";
      break;
    case error.TIMEOUT:
      locationDiv, (innerText = "The request to get user location timed out");
  }
};

const showLocation = async (position) => {
  //We user the nomination Api fro getting actual address from latitude adn longitude
  let response = await fetch(
    `https://nominatim.openstreetmap.org/reverse?lat=${position.coords.latitude}&lon=${position.coords.longitude}&format=json`
  );

  //store response object
  let data = await response.json();
  console.log(data.address.city);
  console.log(data.address.country);
  locationDiv.innerText = `${data.address.city}, ${data.address.country}`;
};

const popup = document.querySelector(".popup");
const close = document.querySelector(".close");

window.onload = function () {
  setTimeout(function () {
    popup.style.display = "block";
  }, 2000);
};

close.addEventListener("click", () => {
  popup.style.display = "none";
});
let availabledoctorId = document.getElementById("doctoravailability");
let bookingscheduleId = document.getElementById("bookingschedule");
let rescheduleId = document.getElementById("reschedule");
let homeBodyId = document.getElementById("homeBody");
let doctoravailpageId = document.getElementById("doctoravailpage");
let bookingschedule = document.getElementById("bookingschedulepage");
let requestscheduleEl = document.getElementById("requestschedule");
let viewappointmentlistEl = document.getElementById("viewappointmentlist");
let reschedulepageEl = document.getElementById("reschedulepage");
let patientgatewayEl = document.getElementById("patientgateway");

function Home() {
    availabledoctorId.classList.remove("underliner");
    bookingscheduleId.classList.remove("underliner");
    rescheduleId.classList.remove("underliner");
}

function onDoctorAvailability() {
    availabledoctorId.classList.add("underliner");
    bookingscheduleId.classList.remove("underliner");
    rescheduleId.classList.remove("underliner");
}

function onBookingSchedule() {
    bookingscheduleId.classList.add("underliner");
    availabledoctorId.classList.remove("underliner");
    rescheduleId.classList.remove("underliner");
   
}

function onReschedulePage() {
    bookingscheduleId.classList.remove("underliner");
    rescheduleId.classList.add("underliner");
    availabledoctorId.classList.remove("underliner");
}



function OnPatientGateWay() {
    availabledoctorId.classList.remove("underliner");
    bookingscheduleId.classList.remove("underliner");
    rescheduleId.classList.remove("underliner");
}

let firstnameEl = document.getElementById("firstname");
let firstnameErrMsgEl = document.getElementById("firstnameErrMsg");
let lastnameEl = document.getElementById("lastname");
let lastnameErrMsgEl = document.getElementById("lastnameErrMsg");
let phonenumberEl = document.getElementById("phonenumber");
let phonenumberErrMsgEl = document.getElementById("phonenumberErrMsg");
let emailEl = document.getElementById("email");
let emailErrMsgEl = document.getElementById("emailErrMsg");
let dobEl = document.getElementById("dob");
let dobErrMsgEl = document.getElementById("dobErrMsg");
let departmentcodeEl = document.getElementById("departmentcode");
let departmentcodeErrMsgEl = document.getElementById("departmentcodeErrMsg");
let myFormEl = document.getElementById("myForm");
let checkBoxEl = document.getElementById("checkbox");
let changevalueEl=document.getElementById("changevalue");
let changeappointeddivEl=document.getElementById("changeappointeddiv")
changeappointeddivEl.classList.add("display")
document.getElementById("changevalue").addEventListener("input", function(event) {
  if(document.getElementById("changevalue").value == "yes"){
      changeappointeddivEl.classList.remove("display")
  }
  if(document.getElementById("changevalue").value == "no"){
      changeappointeddivEl.classList.add("display")
  } 

  });
 let formData = {
     firstname: "",
     lastname: "",
     phonenumber: "",
     email: "",
     dob: "",
    departmentcode: "",
     symptoms:"",
     specific_requirements:"", 
     occupation:""
 };

 firstnameEl.addEventListener("change", function(event) {
    if (event.target.value === "") {
         firstnameErrMsgEl.textContent = "Required*";
     } else {
         firstnameErrMsgEl.textContent = "";
     }

     formData.firstname = event.target.value;
 });

 lastnameEl.addEventListener("change", function(event) {
     if (event.target.value === "") {
         lastnameErrMsgEl.textContent = "Required*";
     } else {
         lastnameErrMsgEl.textContent = "";
     }

     formData.lastname = event.target.value;
 });
 phonenumberEl.addEventListener("change", function(event) {
     if (event.target.value === "") {
         phonenumberErrMsgEl.textContent = "Required*";
     } else {
         phonenumberErrMsgEl.textContent = "";
     }
     formData.phonenumber = event.target.value;
 });
 dobEl.addEventListener("change", function(event) {
     if (event.target.value === "") {
         dobErrMsgEl.textContent = "Required*";
     } else {
         dobErrMsgEl.textContent = "";
     }
     formData.dob = event.target.value;
 });
 departmentcodeEl.addEventListener("change", function(event) {
     if (event.target.value === "") {
         departmentcodeErrMsgEl.textContent = "Required*";
     } else {
         departmentcodeErrMsgEl.textContent = "";
     }

     formData.departmentcode = event.target.value;
 });
 emailEl.addEventListener("change", function(event) {
     formData.email = event.target.value;
 })

function validateFormData(formData) {
     let {
         firstname,
         lastname,
         phonenumber,
         dob,
         departmentcode
     } = formData;
     if (firstname === "") {
         firstnameErrMsgEl.textContent = "Required*";
     }
     if (lastname === "") {
         lastnameErrMsgEl.textContent = "Required*";
     }
     if (phonenumber === "") {
         phonenumberErrMsgEl.textContent = "Required*";
     }
     if (dob === "") {
         dobErrMsgEl.textContent = "Required*"
     }
     if (departmentcode === "") {
         departmentcodeEl.textContent = "Required*"
     }
 }
 myFormEl.addEventListener("submit", function(event) {
    validateFormData(formData);
 });
console.log(formData)

//sign up
function ToggleCheckBox(elem) {
    var TickLine1 = elem.querySelector(".tick>.Tickline1")
    var Tickline2 = elem.querySelector(".tick>.Tickline2")
    if (elem.getAttribute("data-status") == "true") {
        TickLine1.style.opacity = 1
        Tickline2.style.opacity = 1
        elem.setAttribute("data-status", false)

    } else {
        TickLine1.style.opacity = 0
        Tickline2.style.opacity = 0
        elem.setAttribute("data-status", true)


    }
}
//sign in

//Reschedule

// let spinnerEl = document.getElementById("spinner")
// let resultCountriesEl = document.getElementById("resultCountries")
// let searchInput = document.getElementById("search1")
// let searchInputVal = ""
// let countriesList = []

// function createAndAppendCountry(country) {
//     // Creating and appending countryEl to the resultCountriesEl
//     let countryEl = document.createElement("div");
//     countryEl.classList.add("country-card", "col-1", "col-md-5", "mr-auto", "ml-auto", "d-flex", "flex-row");
//     resultCountriesEl.appendChild(countryEl);

//     // Creating and appending countryFlagEl to the countryEl
//     let countryFlagEl = document.createElement("img");
//     countryFlagEl.src = country.flag;
//     countryFlagEl.classList.add("country-flag", "mt-auto", "mb-auto");
//     countryEl.appendChild(countryFlagEl);

//     // Creating and appending countryInfoEl to the countryEl
//     let countryInfoEl = document.createElement("div");
//     countryInfoEl.classList.add("d-flex", "flex-column", "ml-4");
//     countryEl.appendChild(countryInfoEl);

//     // Creating and appending countryNameEl to the countryInfoEl
//     let countryNameEl = document.createElement("p");
//     countryNameEl.textContent = country.name;
//     countryNameEl.classList.add("country-name");
//     countryInfoEl.appendChild(countryNameEl);

//     // Creating and appending countryPopulationEl to the countryInfoEl
//     let countryPopulationEl = document.createElement("p");
//     countryPopulationEl.textContent = country.population;
//     countryPopulationEl.classList.add("country-population");
//     countryInfoEl.appendChild(countryPopulationEl);
// }



// function displaySearchResults() {
//     resultCountriesEl.textContent = "";
//     for (let country of countriesList) {
//         let countryName = country.name;
//         // If the searchInputVal includes in the countryName, creating and appending it to the resultCountriesEl
//         if (countryName.includes(searchInputVal)) {
//             createAndAppendCountry(country);
//         }
//     }
// }

// function getCountries() {
//     let url = "https://apis.ccbp.in/countries-data";
//     let options = {
//         method: "GET"
//     };


//     spinnerEl.classList.remove("d-none");


//     //Making an HTTP request (GET method) using fetch
//     fetch(url, options)
//         .then(function(response) {
//             return response.json();
//         })
//         .then(function(jsonData) {
//             spinnerEl.classList.add("d-none");
//             countriesList = jsonData;
//             displaySearchResults();
//         });
// }

// function onChangeSearchInput(event) {
//     let searchInputVal = event.target.value;
//     displaySearchResults();
// }
// getCountries();
// searchInput.addEventListener("keyup", onChangeSearchInput)
const addBtn = document.querySelector(".add");

const input = document.querySelector(".inp-group");




function addInput(){
        const name =   document.createElement("input");
        name.type ="text";
        name.placeholder = "ENTER YOUR NAME";


        const phone =   document.createElement("input");
        phone.type ="text";
        phone.placeholder = "ENTER YOUR PHONE";


        const address =   document.createElement("input");
        address.type ="text";
        address.placeholder = "ENTER YOUR ADDRESS";

        const btn    =   document.createElement("a");
        btn.className = "delete";
        btn.innerHTML = "&time";

        const flex  =   document.createElement("div");
        flex.className = "flex";

        input.appendChild(flex);
        flex.appendChild(name);
        flex.appendChild(phone);
        flex.appendChild(address);
        flex.appendChild(btn);

}
addBtn.addEventListener("click",addInput )

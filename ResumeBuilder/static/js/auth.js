// Show/hide password :
const password_input = document.getElementById("id_password");
const show_hide_button = document.getElementById("show-hide-button");

const changeVisibility = () => {
    if (password_input){
        if (password_input.type == "password"){
            password_input.type = "text"
            show_hide_button.src = "http://127.0.0.1:8000/static/images/hide.png"
        } else {
            password_input.type = "password"
            show_hide_button.src = "http://127.0.0.1:8000/static/images/eye.png";
        }
    } else{
        const password1_input = document.getElementById("id_password1");
        if (password1_input.type == "password"){
            password1_input.type = "text"
            show_hide_button.src = "http://127.0.0.1:8000/static/images/hide.png"
        } else {
            password1_input.type = "password"
            show_hide_button.src = "http://127.0.0.1:8000/static/images/eye.png";
        }
    }
}
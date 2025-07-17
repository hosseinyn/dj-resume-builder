// Resume share function
const shareResume = (e) => {
    title = e.dataset.title 
    full_name = e.dataset.name
    access_id = e.dataset.access


    const shareData = {
        title: title,
        text: `${full_name}'s Online Resume`,
        url: `http://127.0.0.1:8000/resume/${access_id}`,
    };

    navigator.share(shareData);
}


// Delete resume function
const delete_resume_button = document.getElementById("delete_resume_button");

const deleteResume = (e) => {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete my resume"
        }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
            title: "Deleted!",
            text: "Your resume has been deleted.",
            icon: "success"
            });
            delete_resume_button.click()
        }
    });

}
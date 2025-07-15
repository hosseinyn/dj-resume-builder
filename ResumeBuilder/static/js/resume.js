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
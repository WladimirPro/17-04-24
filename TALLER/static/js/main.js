const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete) {
    const btnarray = Array.from(btnDelete);
    btnarray.forEach((btn)=> {
        btn.addEventListener('click', (e)=>{
            if(!confirm('Estas Seguro de eliminar?')){
                e.preventDefault();
            }
        });
    });
}
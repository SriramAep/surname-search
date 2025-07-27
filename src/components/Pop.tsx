import './Pop.css'

type popProps = {
    name: string,
    poplist: string[]
}

function Pop({name, poplist}: popProps) {

    // TODO: Add a pop up that lists all the elements of this list
    console.log(poplist);

    return (
        <div>
            <p className='popname'>{name}</p>
        </div>
    )
}


export default Pop
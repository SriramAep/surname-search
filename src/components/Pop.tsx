import './Pop.css'

type popProps = {
    name: string,
    poplist: string[]
}

function Pop({name, poplist}: popProps) {

    return (
        <div>
            <p className='popname'>{name}</p>
        </div>
    )
}


export default Pop
import { useState } from 'react'
import './App.css'
import CardList from '../components/CardList'

function App() {

    const [searchTerm, setSearchTerm] = useState('');

    return (
        <>
        <div className='global-background'>
            <div className="background-container">
                <div className="grid-layer"></div>
                <div className="gradient-overlay-1"></div>
                <div className="gradient-overlay-2"></div>
            </div>
        </div>

        <div className='block'>
            <div className='header'>Are you Kamma?</div>
            {/* <h1>Are you Kamma?</h1> */}
            <input className="search-bar" type='search' placeholder='Type here' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
            <CardList searchTerm={searchTerm}/>
        </div>
        </>
    )
}

export default App

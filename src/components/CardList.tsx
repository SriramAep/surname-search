import jsonData from '../surnameData.json';
import Card from './Card';
import './CardList.css';

type GroupedDataType = Record<string, Record<string, string[]>>;
type filter = {
    searchTerm: string;
}

function CardList({searchTerm}: filter) {
    
    const data: GroupedDataType = jsonData;
    
    const cardComponent = Object.entries(data).map(([letter, nameMap]) => {

        const filteredMap: Record<string, string[]> = {};

        for (const [key, value] of Object.entries(nameMap)) {
            if (key.toLowerCase().includes(searchTerm.toLowerCase())) {
                filteredMap[key] = value;
            }
        }

        if(!Object.keys(filteredMap).length) {
            return;
        }

        return (
            <div key={letter} className='card'>
                <h2>{letter}</h2>
                <Card nameMap={filteredMap} />
            </div>
        );
    })

    return (
        <div className='card-table'>
            {cardComponent}
        </div>
    )
}

export default CardList
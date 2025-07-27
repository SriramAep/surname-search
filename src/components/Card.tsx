import Pop from "./Pop";
import './Card.css';

type cardProps = {
    nameMap: Record<string, string[]>;
}

function Card({nameMap}: cardProps) {
    
    const cardDetails = Object.entries(nameMap).map(([name, list]) => {
        return (
            <Pop key={name} name={name} poplist={list}/>
        );
    })
    
    return (
        <div className="sub-card">
            {cardDetails}
        </div>
    )
}

export default Card
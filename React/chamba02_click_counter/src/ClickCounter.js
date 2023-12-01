import { useState } from "react";

function ClickCounter() {
    // *variable, method and initial value
    const[clicks, setClicks] = useState(0);
    
    console.log(clicks);
    return(
        <div>
            <button onClick={() => setClicks(clicks + 1)}>Click</button>
            <div>Has presionado {clicks} veces</div> 
        </div>
        );
}

export default ClickCounter
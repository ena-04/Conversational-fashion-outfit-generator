import { useState, useEffect } from "react";
import '../components/Sidebar.css'

const Header = () =>    {
    return (
        <div className="header">
            <h1>Chats</h1>
        </div>
    )
}

const Conversation = (props) => {
    return (
        <div className="item">
            <h4 onClick={props.handleClick}>{props.value}</h4>
        </div>
    )
}

const Sidebar = (props) => {
    console.log(props.history)
    const [items, setItems] = useState(props.history || [])
    console.log( items)
    return (
        <div className="side-pane">
        <Header />    
        <div className="list">
            {items.length>0 &&  items.map(item => (<Conversation key={item.id}value={item.value} onClick={props.handleClick}/>))}
        </div>
        <button className="chat-button">New Conversation</button>
        </div>
    )
}


export default Sidebar
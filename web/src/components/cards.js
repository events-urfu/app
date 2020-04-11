import React from "react";

const Cards = (props) => {
    return (
        <section>
            <div className="element"></div>
            <div className="event-name">{props.name}</div>
            <div className="out-block">
                <div className="event-time"><p>{props.time}</p></div>
                <div className="event-place"><p>{props.place}</p></div>
            </div>
        </section>
    )
}

export default Cards;

//внешний вид карточки
//задаем название, время и аудиторию
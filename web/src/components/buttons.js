import React from "react";
import Data from "./data";

const Buttons = () => {
    return (
        <div className="in-time">
            <div className="block-week-month-date">
                <button className="nav active" data-target="tab-1">неделя</button>
                <button className="nav" data-target="tab-2">месяц</button>
                <button className="button-data">дата</button>
            </div>
            <Data datetime='19 марта -- 23 июня'/>
        </div>
    )
}

export default Buttons;

//кнопки
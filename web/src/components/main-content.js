import React from "react";
import Cards from "./cards";

const MainContent = () => {
    return (
        <div id="tabs-content">
            <div className="inside-container block active tab-1">
                <Cards name='Дебют первокурсников' time = '19 марта, 19:30' place='ГУК-505'/>
                <Cards name='Мозгобитва' time='23 июня, 10:00' place='Р-109, Р-203'/>
                <Cards />
            </div>


            <div className="inside-container block tab-2 ">
            <Cards name='Мозгобитва' time='23 июня, 10:00' place='Р-109, Р-203' />
            </div>
            <div className="hider-content"></div>
        </div>
    )
}

export default MainContent;

//содержимое карточки
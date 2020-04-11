import React from "react";
import Buttons from './buttons';

import MainContent from "./main-content";

const Main = () => {
    return (
        <main className="main-block">
            <div className="wrapper">
                <Buttons />
                <MainContent />
            </div>
        </main>
    )
}

export default Main;

//обертка основого контента
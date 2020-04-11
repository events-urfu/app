import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Header from "./components/header";
import Main from './components/main';
import Footer from "./components/footer";
import './script';

class SiteView extends React.Component {
    render() {
        return (
            <React.Fragment>
            <Header />
            <Main />
            <Footer />
            </React.Fragment>
        )
    }
}

// ========================================

ReactDOM.render(
    <SiteView />,
    document.getElementById('root')
);

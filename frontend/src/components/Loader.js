import React from 'react'
import { Spinner } from 'react-bootstrap';

function Loader() {
    return <Spinner
        style={{
            height: '50px',
            width: '50px',
            margin: 'auto',
            display: 'block'
        }}
        animation="grow" />
}

export default Loader
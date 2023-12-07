import React from 'react'
import { useSelector } from 'react-redux'
import { useDispatch } from 'react-redux'

const Test = () => {
    const dispatch= useDispatch()
    const data =useSelector(store=>store)
    const addItem=()=>(
        dispatch({type:'ADD_ITEMS'})
    )
    const decItem=()=>(
        dispatch({type:'DEC_ITEMS'})
    )
    return (
    <>
        <h2>The number of items in the store is {data.count} </h2>
        <button onClick={addItem}>Add</button> 
        &nbsp;&nbsp;&nbsp; 
        <button onClick={decItem}>Remove</button>
    </>
  )
}

export default Test
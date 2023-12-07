import React from 'react'
import { useSelector } from 'react-redux'

const Test = () => {
    const data =useSelector(store=>store)
  return (
    <>
    <h2>The number of items in the store is {data.count} </h2>
    </>
  )
}

export default Test
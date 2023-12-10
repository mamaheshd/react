import React from 'react'
import { useSelector } from 'react-redux'
import Form from './Form'
const Student = () => {
    const data= useSelector(store=>store.student)
  return (
    <>
        <h1>
            The name of student is {data.student_name}
        </h1>
        <Form/>
    </>
  )
}

export default Student
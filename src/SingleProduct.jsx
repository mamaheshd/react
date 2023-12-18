import React, {useEffect} from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchSingleProduct } from './actions/productAction'

const SingleProduct = () => {
    const dispatch=useDispatch()
    const data=useSelector(store=>store.product)
    const product=data.product

    useEffect(()=>{
        dispatch(fetchSingleProduct(2))
    },[dispatch])
  return (
    <>
    <h1>{product.title}</h1>
    </>
  )
}

export default SingleProduct
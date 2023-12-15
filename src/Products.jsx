import React,{useEffect} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import { fetchProducts } from './actions/productAction'
const Products = () => {
    const dispatch=useDispatch()
    const productsData= useSelector(store=>store.productsData)
    const products=productsData.products
    useEffect(()=>{
        try{
            dispatch(fetchProducts())
        }
        catch(error){
            console.log('Error in ferching data')
        }
    },[dispatch])
    return (
    <>
        {products && products.map(item=>(
            <h2>{item.title} </h2>
        ))}
    </>
  )
}



export default Products
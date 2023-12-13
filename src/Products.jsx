import React,{useEffect} from 'react'
import { connect } from 'react-redux'
import { fetchProductData } from './actions/productAction'

const Products = ({products,error,fetchProductData}) => {
    useEffect(()=>{
        fetchProductData()
    },[fetchProductData])
    if(error){
        return <h2>Error:{error}</h2>
    }
  return (
    <>
        {products && products.map((item,i)=>(
            <h2>{item.title} </h2>
        )) }
    </>
  )
}

const mapStateToProps=(state)=>({
    products:state.products,
    error:state.error
})

const mapDispatchToProps={
    fetchProductData
}

export default connect(mapStateToProps,mapDispatchToProps)(Products)
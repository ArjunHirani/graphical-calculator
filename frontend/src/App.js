import React, {useState} from 'react';

export default function App(){
  const [expr,setExpr]=useState('');
  const [result,setResult]=useState('');
  const buttons=['7','8','9','/','sin(','4','5','6','*','cos(','1','2','3','-','tan(','0','.','+','^','sqrt(','(',')','%','log(','C','='];

  const click=async(v)=>{
    if(v==='C'){setExpr('');setResult('');return;}
    if(v==='='){
      const res=await fetch('https://graphical-calculator-api.onrender.com/calculate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({expression:expr})});
      const data=await res.json();
      setResult(data.result ?? data.error);
      return;
    }
    setExpr(expr+v);
  }

  return <div className='wrap'>
    <h1>Graphical Calculator</h1>
    <input value={expr} readOnly />
    <div className='result'>{result}</div>
    <div className='grid'>{buttons.map(b=><button key={b} onClick={()=>click(b)}>{b}</button>)}</div>
  </div>
}
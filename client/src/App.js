import React, { useState, useEffect } from "react";

function App() {

  const [data, setData] = useState([{}])


  useEffect(() => {
    fetch("/recommender").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return(
    <div>
      {(typeof data.artists === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.artists.map((artist, i) => (
          <p key={i}>{artist}</p>
        ))
      )}
    </div>
  )
}

export default App
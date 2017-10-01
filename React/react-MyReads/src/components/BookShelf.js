import React, { Component } from 'react'
import { PropTypes } from 'prop-types'
//Components
import Book from './Book'

export default class BookShelf extends Component {

  static propTypes={
    title: PropTypes.string.isRequired,
    books: PropTypes.array,
    onShelfChange: PropTypes.func.isRequired
  }

  render(){
    const books = this.props.books
    return(
      <div className="bookshelf">
        <h2 className="bookshelf-title">{this.props.title}</h2>
        <div className="bookshelf-books">
          <ol className="books-grid">
            {books.map((book,index)=>(
              <Book
                imageURL={book.imageLinks}
                title={book.title}
                author={book.authors}
                key={``.concat(book.id,index)}
                shelf={book.shelf}
                onShelfChange={(shelf)=>{
                this.props.onShelfChange(book.id,shelf)
                }}
              />
            ))}
          </ol>
        </div>
      </div>
    )
  }
}

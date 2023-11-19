// Функция для отображения содержимого корзины
function displayCartItems() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];

    // Очищаем содержимое корзины перед обновлением
    cartItemsContainer.innerHTML = '';

    // Перебираем товары в корзине и добавляем их на страницу
    cartItems.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.innerHTML = `<p>${item.name} - Цена: $${item.price}</p>`;
        cartItemsContainer.appendChild(cartItem);
    });

    // Подсчёт общей стоимости товаров в корзине
    const totalPrice = cartItems.reduce((total, item) => total + item.price, 0);
    document.getElementById('total-price').textContent = `$${totalPrice}`;
}

// Вызов функции для отображения содержимого корзины при загрузке страницы
displayCartItems();

// Обработчик события клика на кнопку "Купить"
document.getElementById('buy-button').addEventListener('click', function() {
    // Получение общей стоимости товаров
    const totalPrice = parseFloat(document.getElementById('total-price').textContent.slice(1)); // Удаляем "$" из начала строки и парсим в число

    // Можно добавить дополнительную логику для завершения покупки, например, отправить заказ на сервер
    // В данном примере просто выведем сообщение в консоль
    console.log(`Поздравляем с покупкой! Общая стоимость: $${totalPrice}`);

    // Очищаем содержимое корзины после покупки
    localStorage.removeItem('cart');
    displayCartItems(); // Обновляем отображение корзины
});
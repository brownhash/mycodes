class PriceCalc{
    private double TaxCalc(int baseAmount){
        double rtoTax, gst, totalTax;
        rtoTax = baseAmount * .12;
        gst = baseAmount * .05;
        totalTax = rtoTax + gst;

        return totalTax;
    }

    protected double CarPrice(int carCost) {
        double tax, totalPrice;
        tax = TaxCalc(carCost);
        totalPrice = tax + carCost;

        return totalPrice;
    }
}

class Car extends PriceCalc{
    protected String brand = "Hyundai";
    PriceCalc price = new PriceCalc();
    double carPrice;

    protected void CarInfo(String modelName){
        if (modelName == "i20"){
            System.out.println("i20\nCC: 1200\nHP: 90\nCost: 8L");
            carPrice = price.CarPrice(800000);
            System.out.println("on-road cost= " + carPrice);
        } else if (modelName == "i10"){
            System.out.println("i10\nCC: 1100\nHP: 80\nCost: 6L");
            carPrice = price.CarPrice(600000);
            System.out.println("on-road cost= " + carPrice);
        }
    }

}

class Mycar extends Car{
    public static void main(String[] args){
        Car CarObject = new Car();
        System.out.println(CarObject.brand);
        CarObject.CarInfo("i20");
    }
}
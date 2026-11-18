
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dealer, Review
from .serializers import DealerSerializer, ReviewSerializer


@api_view(['GET'])
def get_all_dealers(request):
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_dealer_by_id(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        serializer = DealerSerializer(dealer)
        return Response(serializer.data)
    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=404)


@api_view(['GET'])
def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state)
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_dealer_reviews(request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_dealer_review(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)

        name = request.data.get('name')
        review_text = request.data.get('review')
        purchase = request.data.get('purchase', '')

        if not name or not review_text:
            return Response(
                {'error': 'Name and review are required'},
                status=400
            )

        review = Review.objects.create(
            dealer=dealer,
            name=name,
            review=review_text,
            purchase=purchase
        )

        return Response({
            'message': 'Review submitted successfully',
            'id': review.id,
            'dealer_id': dealer.id,
            'name': review.name,
            'review': review.review,
            'purchase': review.purchase
        }, status=201)

    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=404)

    
def home(request):
    dealers = Dealer.objects.all()
    state = request.GET.get('state', '')

    if state:
        dealers = dealers.filter(state__iexact=state)

    return render(request, 'dealers/home.html', {
        'dealers': dealers,
        'state': state
    })


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = dealer.reviews.all().order_by('-created_at')

    return render(request, 'dealers/dealer_detail.html', {
        'dealer': dealer,
        'reviews': reviews
    })


def post_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        review_text = request.POST.get('review', '').strip()
        purchase = request.POST.get('purchase', '').strip()

        if name and review_text:
            Review.objects.create(
                dealer=dealer,
                name=name,
                review=review_text,
                purchase=purchase
            )
            messages.success(request, 'Review posted successfully!')
            return redirect('dealer_detail', dealer_id=dealer.id)

        messages.error(request, 'Please enter your name and review.')

    return render(request, 'dealers/post_review.html', {
        'dealer': dealer
    })

